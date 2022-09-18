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
