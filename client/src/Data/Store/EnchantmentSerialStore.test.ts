import { MockEnchantmentSerialStore } from "./EnchantmentSerialStore";

test('set serialId', () => {
  const store = new MockEnchantmentSerialStore();
  store.initialize();

  expect(store.serialId === store.serials[0].id);

  store.setSerialId(store.serials[1].id);
  expect(store.serialId === store.serials[1].id);
});
