import DataSource from "./DataSource";

test('get serials', () => {
  const source = new DataSource();
  return source.getSerials().then(serials => {
    expect(serials.length > 0).toBeTruthy();
    for (const serial of serials) {
      expect(serial.id !== undefined).toBeTruthy();
      expect(serial.name !== undefined).toBeTruthy();
      expect(serial.des !== undefined).toBeTruthy();
      expect(serial.url !== undefined).toBeTruthy();
      expect(serial.api !== undefined).toBeTruthy();
    }
  });
});

test('get attributes by serialId', () => {
  const source = new DataSource();
  return source.getAttributesBySerialId(1).then(enchantableAttributeRows => {
    expect(enchantableAttributeRows.length > 0).toBeTruthy();
    for (const row of enchantableAttributeRows) {
      expect(row.probability !== 0).toBeTruthy();
      expect(row.rowNumber !== 0).toBeTruthy();
      expect(row.enchantableAttributes.length !== 0).toBeTruthy();

      for (const attribute of row.enchantableAttributes) {
        expect(attribute.isPercentage !== undefined).toBeTruthy();
        expect(attribute.name !== undefined).toBeTruthy();
        expect(attribute.probability !== undefined).toBeTruthy();
        expect(attribute.start !== undefined).toBeTruthy();
        expect(attribute.step !== undefined).toBeTruthy();
        expect(attribute.stop !== undefined).toBeTruthy();
      }
    }
  });
});
