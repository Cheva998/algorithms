/** @param {NS} ns */
export async function main(ns) {
  function getAttrs(target) {
    const attrs = ['maxRam', 'maxMoney', 'minSecurity', 'portsReq', 'minLevel']
    if (this.hasOwnProperty(target)) {
      let ownAttr = Object.keys(this[target])
      if (attrs.every((att) => ownAttr.includes(att))) {
        return 
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
}
