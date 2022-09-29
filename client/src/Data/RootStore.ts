import EnchantableAttributeRowStore from "./Store/EnchantableAttributeRowStore";
import EnchantedUserStore from "./Store/EnchantedUserStore";
import EnchantmentSerialStore from "./Store/EnchantmentSerialStore";

export default class RootStore {
  private enchantmentSerialStore: EnchantmentSerialStore;
  private enchantableAttributeRowStore: EnchantableAttributeRowStore;
  private enchantedUserStore: EnchantedUserStore;

  constructor() {
    this.enchantmentSerialStore = new EnchantmentSerialStore();
    this.enchantableAttributeRowStore = new EnchantableAttributeRowStore(this.enchantmentSerialStore);
    this.enchantedUserStore = new EnchantedUserStore();
    this.enchantmentSerialStore.initialize();
    this.enchantableAttributeRowStore.initialize();
  }
}