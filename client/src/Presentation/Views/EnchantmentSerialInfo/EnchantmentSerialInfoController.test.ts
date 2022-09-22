import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import EnchantmentSerialInfoController from "./EnchantmentSerialInfoController";

class MockEnchantmentSerialStore extends EnchantmentSerialStore {
  initialize() {
    this.serials = [{
      id: 1,
      name: "name1",
      des: "des1",
      url: "url1",
      api: "api1",
    }, {
      id: 2,
      name: "name2",
      des: "des2",
      url: "url2",
      api: "api2",
    }];
    this.serialId = 1;
  }
}

test('get serial', () => {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  enchantmentSerialStore.initialize();
  const controller = new EnchantmentSerialInfoController({ enchantmentSerialStore });
  expect(controller.getSerial()).toStrictEqual({
    serialDescription: "des1",
    serialUrl: "url1",
  });
});

test('set serial id', () => {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  enchantmentSerialStore.initialize();
  const controller = new EnchantmentSerialInfoController({ enchantmentSerialStore });
  controller.setSerialId(2);
  expect(controller.getSerial()).toStrictEqual({
    serialDescription: "des2",
    serialUrl: "url2",
  });
});
