import { action, makeObservable, observable } from "mobx";
import DataSource from "../DataSource";
import { EnchantmentSerial } from "../EnchantmentSerial";

class EnchantmentSerialStore {
  @observable serials: EnchantmentSerial[] = [];
  @observable serialId: number | '' = '';

  constructor() {
    makeObservable(this);
  }

  initialize() {
    const source = new DataSource();
    source.getSerials().then(serials => {
      this.setSerials(serials);
      this.setSerialId(serials[0].id);
    });
  }

  @action setSerialId(serialId: number) {
    this.serialId = serialId;
  }

  @action private setSerials(serials: EnchantmentSerial[]) {
    this.serials = serials;
  }
}

export default EnchantmentSerialStore;