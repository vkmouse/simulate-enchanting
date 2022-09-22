import React from "react";
import { SelectChangeEvent, FormControl, InputLabel, Select, MenuItem } from "@mui/material";
import ComponentData from "./ComponentData";

interface IProps {
  label: string
  data: ComponentData[]
  value: NonNullable<unknown>
  onChange?: (value: NonNullable<unknown>) => void
}

function CustomCombobox(props: IProps) {
  const { label, data, value, onChange } = props;

  const handleChange = (event: SelectChangeEvent<NonNullable<unknown>>) => {
    if (onChange !== undefined) {
      onChange(event.target.value);
    }
  };

  return (
    <FormControl sx={{ m: 1, minWidth: 125, margin: 0, marginLeft: 1 }} size="small">
      <InputLabel>{label}</InputLabel>
      <Select value={value} label={label} onChange={handleChange} >
        <MenuItem value={''}>
            <em>None</em>
        </MenuItem>
        {data.map(p =>
          <MenuItem key={p.name} value={p.value as string}>
            {p.name}
          </MenuItem>
        )}
      </Select>
    </FormControl>
  );
}

export default CustomCombobox;