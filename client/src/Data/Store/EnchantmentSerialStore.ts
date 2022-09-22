import DataSource from "../DataSource";
import { EnchantmentSerial } from "../EnchantmentSerial";

class EnchantmentSerialStore {
  serials: EnchantmentSerial[];
  currentSerialId: number;

  constructor() {
    this.serials = [];
    this.currentSerialId = -1;
  }

  initialize() {
    const source = new DataSource();
    source.getSerials().then(this.setSerials);
    this.currentSerialId = this.serials[0].id;
  }

  private setSerials(serials: EnchantmentSerial[]) {
    this.serials = serials;
  }

  setCurrentSerialId(serialId: number) {
    this.currentSerialId = serialId;
  }
}

export default EnchantmentSerialStore;