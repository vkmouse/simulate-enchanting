import EnchantableAttributeRowStore from "./Store/EnchantableAttributeRowStore";
import EnchantmentSerialStore from "./Store/EnchantmentSerialStore";

export default class RootStore {
  private enchantmentSerialStore: EnchantmentSerialStore;
  private enchantableAttributeRowStore: EnchantableAttributeRowStore;

  constructor() {
    this.enchantmentSerialStore = new EnchantmentSerialStore();
    this.enchantableAttributeRowStore = new EnchantableAttributeRowStore(this.enchantmentSerialStore);
    this.enchantmentSerialStore.initialize();
    this.enchantableAttributeRowStore.initialize();
  }
}