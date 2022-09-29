import { TableContainer, Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";
import React from "react";

interface IProps {
  stats: string[][]
}

class EnchantmentStatsView extends React.Component<IProps> {
  render() {
    const { stats } = this.props;
    return (
      <div className='wrapper'>
        <div className='wrapper__title'>附魔統計</div>
        <div className='wrapper__content'>
          <TableContainer sx={{ height: 300 }}>
            <Table size='small'>
              <TableHead>
                <TableRow>
                  <TableCell>第一欄</TableCell>
                  <TableCell>第二欄</TableCell>
                  <TableCell>第三欄</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {stats.map((p, index) => {
                  return (
                    <TableRow key={index}>
                      <TableCell>{p.length > 0 ? p[0] : ''}</TableCell>
                      <TableCell>{p.length > 1 ? p[1] : ''}</TableCell>
                      <TableCell>{p.length > 2 ? p[2] : ''}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </TableContainer>  
        </div>
      </div>
    );
  }
}

export default EnchantmentStatsView;