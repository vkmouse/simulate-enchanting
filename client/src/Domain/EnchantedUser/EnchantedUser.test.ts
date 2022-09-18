import EnchantedUser from "./EnchantedUser";

function createUser() {
  return new EnchantedUser([{
    enchantableAttributes: [{
      name: 'First Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }, {
      name: 'Second Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }],
    rowNumber: 1,
    probability: 1.0
  }, {
    enchantableAttributes: [{
      name: 'Third Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }, {
      name: 'Fourth Attribute',
      isPercentage: true,
      start: 1,
      stop: 2,
      step: 1,
      probability: 0.5
    }],
    rowNumber: 2,
    probability: 1.0
  }]);
}

test('enchant until times reached', () => {
  const user = createUser();
  const results = user.enchantUntilTimesReached(13);
  expect(results.length).toBe(13);
});

test('enchant until target reached', () => {
  const user = createUser();
  const results = user.enchantUntilTargetReached([{
    name: 'Third Attribute',
    isPercentage: true,
    value: 2,
  }]);
  expect(results[results.length - 1][1]).toStrictEqual({
    name: 'Third Attribute',
    isPercentage: true,
    value: 2,
    rowNumber: 2
  });
});
