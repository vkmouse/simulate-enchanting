import React from "react";
import ComponentData from "../../Components/ComponentData";
import TabPanel from "../../Components/CustomTabPanel";
import CustomToggleButton from "../../Components/CustomToggleButton";

interface IProps {
  enchantmentMethodData: ComponentData[]
  enchantmentMethod: NonNullable<unknown>
  onEnchantmentMethodChange?: (value: NonNullable<unknown>) => void
}

class EnchantmentSimulationView extends React.Component<IProps> {
  render() {
    const { 
      enchantmentMethodData, 
      enchantmentMethod, 
      onEnchantmentMethodChange 
    } = this.props;

    return (
      <div className='wrapper'>
        <div className='wrapper__title'>模擬附魔</div>
        <div className='wrapper__content'>
          <CustomToggleButton
            data={enchantmentMethodData}
            value={enchantmentMethod}
            toggleButtonProps={{ sx: { fontSize: 16, lineHeight: 1.2 } }}
            onChange={onEnchantmentMethodChange}
          />
          <TabPanel 
            index={enchantmentMethodData[0].value} 
            value={enchantmentMethod}
          >
            Page 1
          </TabPanel>
          <TabPanel 
            index={enchantmentMethodData[1].value} 
            value={enchantmentMethod}
          >
            Page 2
          </TabPanel>
        </div>
      </div>
    );
  }
}

export default EnchantmentSimulationView;