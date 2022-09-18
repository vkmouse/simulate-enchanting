import DataSource from "../DataSource";
import { EnchantmentSerial } from "../EnchantmentSerial";

class EnchantmentSerialStore {
  serials: EnchantmentSerial[];

  constructor() {
    const source = new DataSource();
    this.serials = [];
    source.getSerials().then(this.setSerials);
  }

  private setSerials(serials: EnchantmentSerial[]) {
    this.serials = serials;
  }
}

export default EnchantmentSerialStore;