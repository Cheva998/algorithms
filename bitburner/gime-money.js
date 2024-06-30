/** @param {NS} ns */
export async function main(ns) {
  let target = ns.args[0];
  let monThresh = ns.getServerMaxMoney(target) * 0.8;
  let secThresh = ns.getServerMinSecurityLevel(target) + 5;
  while(true) {
    if (ns.getServerSecurityLevel(target) > secThresh) {
      await ns.weaken(target);
    } else if (ns.getServerMoneyAvailable(target) < monThresh) {
      await ns.grow(target);
    } else {
      await ns.hack(target);
    }
  }
}
