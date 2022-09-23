import { MockEnchantableAttributeRowStore } from "../../../Data/Store/EnchantableAttributeRowStore";
import { MockEnchantmentSerialStore } from "../../../Data/Store/EnchantmentSerialStore";
import EnchantableAttributeInfoController from "./EnchantableAttributeInfoController";

function createController() {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  const enchantableAttributeRowStore = new MockEnchantableAttributeRowStore(enchantmentSerialStore);
  enchantmentSerialStore.initialize();
  enchantableAttributeRowStore.initialize();
  enchantmentSerialStore.setSerialId(2);
  const controller = new EnchantableAttributeInfoController({ 
    enchantmentSerialStore,
    enchantableAttributeRowStore
  });
  return { 
    controller,
    enchantmentSerialStore,
    enchantableAttributeRowStore
  };
}

test('set row number', () => {
  const { controller } = createController();
  expect(controller.rowNumber).toBe(1);

  controller.setRowNumber(2);
  expect(controller.rowNumber).toBe(2);

  controller.setRowNumber(3);
  expect(controller.rowNumber).toBe(2);
});

test('reset row number when change serial', () => {
  const { enchantmentSerialStore, controller } = createController();
  expect(controller.rowNumber).toBe(1);

  controller.setRowNumber(2);
  expect(controller.rowNumber).toBe(2);

  enchantmentSerialStore.setSerialId(1);
  expect(controller.rowNumber).toBe(1);
});

test('row data', () => {
  const { 
    enchantmentSerialStore, 
    controller 
  } = createController();

  expect(controller.rowData).toStrictEqual([
    { name: '第一欄', value: 1 },
    { name: '第二欄', value: 2 },
  ]);

  enchantmentSerialStore.setSerialId(1);
  expect(controller.rowData).toStrictEqual([
    { name: '第一欄', value: 1 },
  ]);
});

test('row probability', () => {
  const { 
    enchantmentSerialStore, 
    controller 
  } = createController();

  expect(controller.rowProbability).toBe(60);

  controller.setRowNumber(2);
  expect(controller.rowProbability).toBe(70);

  enchantmentSerialStore.setSerialId(1);
  expect(controller.rowProbability).toBe(50);
});

