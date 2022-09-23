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

export class MockEnchantmentSerialStore extends EnchantmentSerialStore {
  initialize() {
    this.serials = [{
      id: 1,
      name: "name1",
      des: "des1",
      url: "url1",
      api: "api1",
    }, {
      id: 2,
      name: "name2",
      des: "des2",
      url: "url2",
      api: "api2",
    }];
    this.serialId = 1;
  }
}

export default EnchantmentSerialStore;