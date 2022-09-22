import { EnchantmentSerial } from "../../../Data/EnchantmentSerial";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";
import ComponentData from "../../Components/ComponentData";

interface IProps {
  enchantmentSerialStore: EnchantmentSerialStore
}

class EnchantmentSerialInfoController {
  props: IProps;

  constructor(props: IProps) {
    this.props = props;
  }

  setCurrentSerialId(id: number) {
    this.props.enchantmentSerialStore.setCurrentSerialId(id);
  }

  getSerialData(): ComponentData[] {
    return this.props.enchantmentSerialStore.serials.map(p => {
      return {
        name: p.name,
        value: p.id
      };
    });
  }

  getSerial(): EnchantmentSerial {
    const found = this.props.enchantmentSerialStore.serials.find(
      p => p.id === this.props.enchantmentSerialStore.currentSerialId);
    if (found) {
      return found;
    } else {
      throw ('No find');
    }
  }
}

export default EnchantmentSerialInfoController;