import { EnchantmentSerial } from "./EnchantmentSerial";

class DataSource {
  private url = 'https://jwp63667.pythonanywhere.com';

  getSerials(): Promise<EnchantmentSerial[]> {
    return fetch(`${this.url}/serials`)
    .then(response => response.json())
    .then(serials => {
      const output: EnchantmentSerial[] = [];
      for (const serial of serials) {
        output.push({
          id: serial['Id'],
          name: serial['Name'],
          des: serial['Des'],
          url: serial['Url'],
          api: serial['API'],
        });
      }
      return output;
    });
  }
}

export default DataSource;