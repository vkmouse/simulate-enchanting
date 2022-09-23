import { MockEnchantmentSerialStore } from "../../../Data/Store/EnchantmentSerialStore";
import EnchantmentSerialInfoController from "./EnchantmentSerialInfoController";

function createController() {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  enchantmentSerialStore.initialize();
  const controller = new EnchantmentSerialInfoController({ enchantmentSerialStore });
  return { 
    controller,
    enchantmentSerialStore
  };
}

test('get serial', () => {
  const { enchantmentSerialStore, controller } = createController();
  expect(controller.getSerial()).toStrictEqual({
    serialDescription: enchantmentSerialStore.serials[0].des,
    serialUrl: enchantmentSerialStore.serials[0].url,
  });
});

test('set serial id', () => {
  const { enchantmentSerialStore, controller } = createController();
  controller.setSerialId(enchantmentSerialStore.serials[1].id);
  expect(controller.getSerial()).toStrictEqual({
    serialDescription: enchantmentSerialStore.serials[1].des,
    serialUrl: enchantmentSerialStore.serials[1].url,
  });
});
