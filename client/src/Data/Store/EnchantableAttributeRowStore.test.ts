import { MockEnchantableAttributeRowStore } from "./EnchantableAttributeRowStore";
import { MockEnchantmentSerialStore } from "./EnchantmentSerialStore";

test('auto update rows', () => {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  const enchantableAttributeRowStore = new MockEnchantableAttributeRowStore(enchantmentSerialStore);
  enchantmentSerialStore.initialize();

  expect(enchantableAttributeRowStore.rows.length).toBe(0);

  enchantableAttributeRowStore.initialize();
  expect(enchantableAttributeRowStore.rows.length).toBe(1);

  enchantmentSerialStore.setSerialId(2);
  expect(enchantableAttributeRowStore.rows.length).toBe(2);
});
