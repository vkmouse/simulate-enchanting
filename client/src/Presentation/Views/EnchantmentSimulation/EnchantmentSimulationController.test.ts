import { EnchantingTerminationCondition } from "../../../Core/Core";
import EnchantedUserStore from "../../../Data/Store/EnchantedUserStore";
import EnchantmentSimulationController from "./EnchantmentSimulationController";

function createController() {
  const enchantedUserStore = new EnchantedUserStore();
  const controller = new EnchantmentSimulationController({ enchantedUserStore });
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
