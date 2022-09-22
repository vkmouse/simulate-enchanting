import { action, makeObservable, observable } from "mobx";
import DataSource from "../DataSource";
import { EnchantmentSerial } from "../EnchantmentSerial";

class EnchantmentSerialStore {
  @observable serials: EnchantmentSerial[] = [];
  @observable currentSerialId: number | '';

  constructor() {
    makeObservable(this);
    this.serials = [];
    this.currentSerialId = '';
  }

  initialize() {
    const source = new DataSource();
    source.getSerials().then(serials => {
      this.setSerials(serials);
      this.setCurrentSerialId(serials[0].id);
    });
  }

  @action setCurrentSerialId(serialId: number) {
    this.currentSerialId = serialId;
  }

  @action private setSerials(serials: EnchantmentSerial[]) {
    this.serials = serials;
  }
}

export default EnchantmentSerialStore;