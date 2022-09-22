import { EnchantmentSerial } from "../../../Data/EnchantmentSerial";
import EnchantmentSerialStore from "../../../Data/Store/EnchantmentSerialStore";

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