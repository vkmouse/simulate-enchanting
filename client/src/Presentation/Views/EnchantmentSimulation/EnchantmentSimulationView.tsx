import React from "react";
import ComponentData from "../../Components/ComponentData";
import TabPanel from "../../Components/CustomTabPanel";
import ToggleButton from "../../Components/CustomToggleButton";

interface IProps {
  enchantmentMethodData: ComponentData[]
  condition: NonNullable<unknown>
  onEnchantmentMethodChange?: (value: NonNullable<unknown>) => void
}

class EnchantmentSimulationView extends React.Component<IProps> {
  render() {
    const { 
      enchantmentMethodData, 
      condition, 
      onEnchantmentMethodChange 
    } = this.props;

    return (
      <div className='wrapper'>
        <div className='wrapper__title'>模擬附魔</div>
        <div className='wrapper__content'>
          <ToggleButton
            data={enchantmentMethodData}
            value={condition}
            toggleButtonProps={{ sx: { fontSize: 16, lineHeight: 1.2 } }}
            onChange={onEnchantmentMethodChange}
          />
          <TabPanel 
            index={enchantmentMethodData[0].value} 
            value={condition}
          >
            Page 1
          </TabPanel>
          <TabPanel 
            index={enchantmentMethodData[1].value} 
            value={condition}
          >
            Page 2
          </TabPanel>
        </div>
      </div>
    );
  }
}

export default EnchantmentSimulationView;