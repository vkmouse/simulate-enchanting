import { EnchantedAttributeRow } from "../../Core/Core";
import EnchantedStatsStore from "./EnchantedStatsStore";

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
      value: 8,
      rowNumber: 1
    }]
  ];
}

test('push stats', () => {
  const enchantedStatsStore = new EnchantedStatsStore(999);
  expect(enchantedStatsStore.stats.length).toBe(0);
  const data = createData();

  enchantedStatsStore.pushStats([data[0]]);
  expect(enchantedStatsStore.stats.length).toBe(1);
  expect(enchantedStatsStore.stats[0]).toStrictEqual(data[0]);

  enchantedStatsStore.pushStats([data[1]]);
  expect(enchantedStatsStore.stats.length).toBe(2);
  expect(enchantedStatsStore.stats[1]).toStrictEqual(data[1]);
});

test('clear', () => {
  const enchantedStatsStore = new EnchantedStatsStore(999);
  expect(enchantedStatsStore.stats.length).toBe(0);
  const data = createData();

  enchantedStatsStore.pushStats(data);
  expect(enchantedStatsStore.stats.length).toBe(3);

  enchantedStatsStore.clear();
  expect(enchantedStatsStore.stats.length).toBe(0);
});

test('max recording', () => {
  const enchantedStatsStore = new EnchantedStatsStore(2);
  expect(enchantedStatsStore.stats.length).toBe(0);
  const data = createData();

  enchantedStatsStore.pushStats([data[0], data[1]]);
  expect(enchantedStatsStore.stats.length).toBe(2);
  expect(enchantedStatsStore.stats[0]).toStrictEqual(data[0]);
  expect(enchantedStatsStore.stats[1]).toStrictEqual(data[1]);

  enchantedStatsStore.pushStats([data[2]]);
  expect(enchantedStatsStore.stats.length).toBe(2);
  expect(enchantedStatsStore.stats[0]).toStrictEqual(data[1]);
  expect(enchantedStatsStore.stats[1]).toStrictEqual(data[2]);
});

test('push out of limit', () => {
  const enchantedStatsStore = new EnchantedStatsStore(2);
  expect(enchantedStatsStore.stats.length).toBe(0);
  const data = createData();

  enchantedStatsStore.pushStats(data);
  expect(enchantedStatsStore.stats.length).toBe(2);
  expect(enchantedStatsStore.stats[0]).toStrictEqual(data[1]);
  expect(enchantedStatsStore.stats[1]).toStrictEqual(data[2]);
});
