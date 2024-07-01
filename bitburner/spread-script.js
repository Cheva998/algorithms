/** @param {NS} ns */
export async function main(ns) {
  let scriptName = 'give-money.js';
  let ramCost = ns.getScriptRam(scriptName);
  
  function getAttrs(target) {
    const attrs = ['maxRam', 'maxMoney', 'minSecurity', 'portsReq', 'minLevel']
    if (this.hasOwnProperty(target)) {
      let ownAttr = Object.keys(this[target])
      if (attrs.every((att) => ownAttr.includes(att))) {
        return ;
      }
    }
    this[target] = {};
    this[target]['maxRam'] = ns.getServerMaxRam(target);
    this[target]['maxMoney'] = ns.getServerMaxMoney(target);
    this[target]['minSecurity'] = ns.getServerMinSecurityLevel(target);
    this[target]['portsReq'] = ns.getServerNumPortsRequired(target);
    this[target]['minLevel'] = ns.getServerRequiredHackingLevel(target); 
  }

  function findServers(serversInfo = {}) {
    let servers = ns.scan();
    servers.forEach(getAttrs, serversInfo)
    return serversInfo;
  }

  function getAvailableExploits() {
    let listExploits = ['brutessh','ftpcrack','relaysmtp','sqlinject','httpworm']
    listExploits = listExploits.filter(file => ns.fileExists(`${file}.exe`));
    return listExploits
  }
  function findHackable(serversInfo) {
    let servers = {};
    let listExploits = getAvailableExploits();
    let hackLevel = ns.getHackingLevel();
    for (let serv in serversInfo) {
      if (serversInfo[serv].minLevel <= hackLevel && 
        serversInfo[serv].portsReq <= listExploits.length &&
        serversInfo[serv].maxMoney >= 100) {
          servers[serv] = serversInfo[serv]
        }
    }
    return servers;
  }

  function nukeServer(serversInfo) {
    let servers = {}
    let allExploits = {
      'brutessh': ns.brutessh,
      'ftpcrack': ns.ftpcrack,
      'relaysmtp': ns.relaysmtp,
      'sqlinject': ns.sqlinject,
      'httpworm': ns.httpworm
      }
    let listExploits = getAvailableExploits();
    for (let serv in serversInfo) {
      servers[serv] = serversInfo[serv]
      if (serv.nuked) {
        continue
      }
      for (let hack_i of listExploits){
        allExploits[hack_i](serv)
      }
      ns.nuke(serv)
      servers[serv]['nuked'] = true; 
    }
    return servers;
  }

  function spreadScript(serversInfo) {
    let numThreads;
    let startCode;
    for (let serv in serversInfo) {
      if (ns.isRunning(scriptName, serv)) {
        ns.tprint(`File ${scriptName} already running on ${serv} server`)
        continue;
      }
      numThreads = Math.floor(serversInfo[serv].maxRam / ramCost);
      ns.scp(scriptName, serv);
      startCode = ns.exec(scriptName, serv, numThreads, serv);
      ns.tprint(`Program${startCode > 0 ? ' ' : ' NOT '}started on server ${serv} with code ${startCode}`)
    }
  }

  let servs = findServers()
  servs = findHackable(servs)
  servs = nukeServer(servs)
  spreadScript(servs);
}
