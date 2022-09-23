import { EnchantableAttributeRow } from "../Core/Core";
import { EnchantmentSerial } from "./EnchantmentSerial";

class DataSource {
  private url = 'https://jwp63667.pythonanywhere.com';

  getSerials(): Promise<EnchantmentSerial[]> {
    return fetch(`${this.url}/serials`)
    .then(response => response.json())
    .then(receive => {
      const serials: EnchantmentSerial[] = [];
      for (const serial of receive) {
        serials.push({
          id: serial['Id'],
          name: serial['Name'],
          des: serial['Des'],
          url: serial['Url'],
          api: serial['API'],
        });
      }
      return serials;
    });
  }

  getAttributesBySerialId(serialId: number) {
    return fetch(`${this.url}/attributes?serial_id=${serialId}`)
    .then(response => response.json())
    .then(receive => {
      const rows: EnchantableAttributeRow[] = [];
      for (const attribute of receive) {
        let row = rows.find(p => p.rowNumber === attribute['Row']['RowNumber']);
        if (row === undefined) {
          row = {
            enchantableAttributes: [],
            rowNumber: attribute['Row']['RowNumber'],
            probability: attribute['Row']['Probability']
          };
          rows.push(row);
        }

        row.enchantableAttributes.push({
          isPercentage: attribute['Category']['IsPercentage'],
          name: attribute['Category']['Name'],
          probability: attribute['Probability'],
          start: attribute['Range']['Start'],
          stop: attribute['Range']['Stop'],
          step: attribute['Range']['Step'],
        });
      }
      return rows;
    });
  }
}

export default DataSource;