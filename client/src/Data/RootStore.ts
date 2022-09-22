import EnchantmentSerialStore from "./Store/EnchantmentSerialStore";

export default class RootStore {
  private enchantmentSerialStore =  new EnchantmentSerialStore();

  constructor() {
    this.enchantmentSerialStore.initialize();
  }
}