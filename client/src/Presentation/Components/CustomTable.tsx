import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TablePagination, TableRow } from "@mui/material";
import React from "react";

interface IProps {
  columes: string[]
  rows: string[][]
  rowsWidth?: string[]
  rowsPerPageOptions?: number[]
}

interface IState {
  page: number
  rowsPerPage: number
}

class CustomTable extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      page: 0,
      rowsPerPage: 5
    };
  }

  tableCells = (elements: string[]): JSX.Element[] => {
    const { rowsWidth } = this.props;
    if (rowsWidth === undefined || rowsWidth.length !== elements.length) {
      return elements.map((element, index) => {  
        return (<TableCell key={index}>{element}</TableCell>);
      });
    } else {
      return elements.map((element, index) => {  
        return (<TableCell key={index} width={rowsWidth[index]}>{element}</TableCell>);
      });
    }
  };

  emptyRows = () => {
    const { page, rowsPerPage } = this.state;
    const { rows } = this.props;
    const emptyRows =
      page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;
    
    if (emptyRows > 0) {
      return (
        <TableRow style={{ height: 33 * emptyRows }} >
          <TableCell colSpan={6} />
        </TableRow>
      );
    } else {
      return undefined;
    }
  };

  handleChangePage = (event: unknown, newPage: number) => {
    this.setState({ page: newPage });
  };

  handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ 
      page: 0,
      rowsPerPage: parseInt(event.target.value, 10)
    });
  };

  render() {
    const { columes, rows, rowsPerPageOptions } = this.props;
    const { page, rowsPerPage } = this.state;

    return (
      <Paper>
        <TableContainer>
          <Table size='small'>
            <TableHead>
              <TableRow>
                {this.tableCells(columes)}
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((row, index) => {
                  return (
                    <TableRow key={index}>
                      {this.tableCells(row)}
                    </TableRow>
                  );
              })}
              {this.emptyRows()}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={rowsPerPageOptions ?? [5, 10, 25]}
          component="div"
          count={rows.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={this.handleChangePage}
          onRowsPerPageChange={this.handleChangeRowsPerPage}
        />
      </Paper>
    );
  }
}

export default CustomTable;