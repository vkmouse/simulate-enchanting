import { Box } from '@mui/material';
import React from 'react';
import ComponentData from '../../Components/ComponentData';
import Button from '../../Components/CustomButton';
import Combobox from '../../Components/CustomCombobox';

interface IProps {
  serialId: NonNullable<unknown>
  serialDescription: string
  serialUrl: string
  serialData: ComponentData[]
  onSerialChange?: (value: NonNullable<unknown>) => void
}

class EnchantmentSerialInfoView extends React.Component<IProps> {
  render() {
    const { 
      serialId, 
      serialDescription,
      serialUrl,
      serialData,
      onSerialChange 
    } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔系列</div>
        <div className='wrapper__content'>
          <div className='wrapper__row'>
            <Combobox 
              label='系列名稱'
              data={serialData}
              value={serialId}
              onChange={onSerialChange}
            />
            <a 
              style={{ textDecoration: "none", }} 
              target={"_blank"} 
              rel="noopener noreferrer" 
              href={serialUrl}
            >
              <Button label='前往官方網站'/>
            </a>
          </div>
          <Box sx={{ 
            margin: '0.5em', 
            marginTop: '1em',
            '&:hover .child': {
              textOverflow: "clip", 
              overflow: "visible" ,
              whiteSpace: "normal"
            }
          }}>
            <Box sx={{ fontWeight: 'bold' }}>內容說明</Box>
            <Box className={"child"} sx={{ 
              cursor: "default",
              marginTop: '0.5em', 
              marginBottom: '0.5em', 
              textOverflow: "ellipsis", 
              overflow: "hidden" ,
              whiteSpace: "nowrap"
            }}>
              {serialDescription}
            </Box>
          </Box>
        </div>
      </div>
    );
  }
}

export default EnchantmentSerialInfoView;