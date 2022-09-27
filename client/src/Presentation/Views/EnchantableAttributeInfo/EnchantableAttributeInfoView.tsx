import { TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';
import React from 'react';
import ComponentData from '../../Components/ComponentData';
import ToggleButton from '../../Components/CustomToggleButton';
import EnchantableAttributeInfo from './EnchantableAttributeInfo';

interface IProps {
  attributes: EnchantableAttributeInfo[]
  rowData: ComponentData[]
  rowNumber: number
  rowProbability: number
  onRowNumberChange?: (value: NonNullable<unknown>) => void
}

class EnchantableAttributeInfoView extends React.Component<IProps> {
  render() {
    const { 
      attributes,
      rowData, 
      rowNumber, 
      rowProbability, 
      onRowNumberChange 
    } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔屬性</div>
        <div className='wrapper__content'>
          <div className='wrapper__row'>
            <ToggleButton
              data={rowData}
              value={rowNumber}
              toggleButtonProps={{ sx: { fontSize: 16, lineHeight: 1.2 } }}
              onChange={onRowNumberChange}
            />
            <div>
              <div>附魔欄位機率: {rowProbability}%</div>
            </div>
          </div>
          <div className='wrapper__row'>
            <TableContainer sx={{ height: 300 }}>
              <Table size='small'>
                <TableHead>
                  <TableRow>
                    <TableCell>屬性名稱</TableCell>
                    <TableCell width="52px">機率</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {attributes.map(p =>
                    <TableRow key={p.name}>
                      <TableCell>{p.name}</TableCell>
                      <TableCell>{p.probability}%</TableCell>
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </TableContainer>    
          </div>
        </div>
      </div>
    );
  }
}

export default EnchantableAttributeInfoView;