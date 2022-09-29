import EnchantableAttributeRowStore from "./Store/EnchantableAttributeRowStore";
import EnchantedStatsStore from "./Store/EnchantedStatsStore";
import EnchantedUserStore from "./Store/EnchantedUserStore";
import EnchantmentSerialStore from "./Store/EnchantmentSerialStore";

export default class RootStore {
  private enchantmentSerialStore: EnchantmentSerialStore;
  private enchantableAttributeRowStore: EnchantableAttributeRowStore;
  private enchantedUserStore: EnchantedUserStore;
  private enchantedStatsStore: EnchantedStatsStore;

  constructor() {
    this.enchantmentSerialStore = new EnchantmentSerialStore();
    this.enchantableAttributeRowStore = new EnchantableAttributeRowStore(this.enchantmentSerialStore);
    this.enchantedUserStore = new EnchantedUserStore();
    this.enchantedStatsStore = new EnchantedStatsStore(999);
    this.enchantmentSerialStore.initialize();
    this.enchantableAttributeRowStore.initialize();
  }
}