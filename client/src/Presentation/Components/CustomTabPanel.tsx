import React from "react";
import { Box } from "@mui/material";

interface TabPanelProps {
  children?: React.ReactNode;
  index: NonNullable<unknown>;
  value: NonNullable<unknown>;
}

class CustomTabPanel extends React.Component<TabPanelProps> {
  render() {
    const { children, value, index, ...other } = this.props;
    return (
      <div
        role="tabpanel"
        hidden={value !== index}
        id={`simple-tabpanel-${index}`}
        aria-labelledby={`simple-tab-${index}`}
        {...other}
      >
        {value === index && (
          <Box sx={{ p: 3 }}>
            {children}
          </Box>
        )}
      </div>
    );
  }
}

export default CustomTabPanel;