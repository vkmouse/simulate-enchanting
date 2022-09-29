import { EnchantedAttributeRow } from "../../../Core/Core";
import EnchantedStatsStore from "../../../Data/Store/EnchantedStatsStore";
import EnchantmentStatsController from "./EnchantmentStatsController";

function createData(): EnchantedAttributeRow[][] {
  return [
    [{
      name: "name1",
      isPercentage: true,
      value: 12,
      rowNumber: 1
    }],
    [{
      name: "name2",
      isPercentage: false,
      value: 6,
      rowNumber: 1
    }],
    [{
      name: "name3",
      isPercentage: false,
      value: -8,
      rowNumber: 1
    }]
  ];
}

function createController() {
  const enchantedStatsStore = new EnchantedStatsStore(999);
  const controller = new EnchantmentStatsController({ enchantedStatsStore });
  return { 
    controller,
    enchantedStatsStore
  };
}

test('convert attribute row to string', () => {
  const { controller } = createController();
  const data = createData();

  expect(controller.convertAttributeRowToString(data[0][0])).toBe("name1 +12%");
  expect(controller.convertAttributeRowToString(data[1][0])).toBe("name2 +6");
  expect(controller.convertAttributeRowToString(data[2][0])).toBe("name3 -8");
});


test('stats auto update', () => {
  const { enchantedStatsStore, controller } = createController();
  const data = createData();

  expect(enchantedStatsStore.stats.length).toBe(0);
  expect(controller.stats.length).toBe(0);

  enchantedStatsStore.pushStats([data[0]]);
  expect(controller.stats.length).toBe(1);
  expect(controller.stats[0]).toStrictEqual(["name1 +12%"]);

  enchantedStatsStore.pushStats([data[1]]);
  expect(controller.stats.length).toBe(2);
  expect(controller.stats[1]).toStrictEqual(["name2 +6"]);
});