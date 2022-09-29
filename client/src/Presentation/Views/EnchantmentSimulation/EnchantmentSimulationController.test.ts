import { EnchantingTerminationCondition } from "../../../Core/Core";
import { MockEnchantableAttributeRowStore } from "../../../Data/Store/EnchantableAttributeRowStore";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";
import EnchantedUserStore from "../../../Data/Store/EnchantedUserStore";
import { MockEnchantmentSerialStore } from "../../../Data/Store/EnchantmentSerialStore";
import EnchantmentSimulationController from "./EnchantmentSimulationController";

function createController() {
  const enchantmentSerialStore = new MockEnchantmentSerialStore();
  const enchantableAttributeRowStore = new MockEnchantableAttributeRowStore(enchantmentSerialStore);
  const enchantedUserStore = new EnchantedUserStore();
  const enchantedStatsStore = new EnchantedStatsStore(999);
  enchantmentSerialStore.initialize();
  enchantableAttributeRowStore.initialize();
  enchantmentSerialStore.setSerialId(2);
  const controller = new EnchantmentSimulationController({ 
    enchantableAttributeRowStore, 
    enchantedUserStore,
    enchantedStatsStore
  });
  return { 
    controller,
    enchantedUserStore
  };
}

test('get enchantment method data', () => {
  const { controller } = createController();
  expect(controller.getEnchantmentMethodData()).toStrictEqual([{
    name: "次數附魔",
    value: EnchantingTerminationCondition.TimesReached
  }, {
    name: "目標附魔",
    value: EnchantingTerminationCondition.TargetReached
  }]);
});

test('set enchantment method', () => {
  const { enchantedUserStore, controller } = createController();
  expect(enchantedUserStore.condition).toBe(EnchantingTerminationCondition.TimesReached);
  
  controller.setEnchantmentMethod(EnchantingTerminationCondition.TargetReached);
  expect(enchantedUserStore.condition).toBe(EnchantingTerminationCondition.TargetReached);
});

test('set times', () => {
  const { enchantedUserStore, controller } = createController();
  expect(enchantedUserStore.times).toBe(1);
  
  controller.setTimes(100);
  expect(enchantedUserStore.times).toBe(100);
});
