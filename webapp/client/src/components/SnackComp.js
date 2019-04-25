import React from "react";
import { Frame, Words } from "@arwes/arwes";


export default ({ children, style }) => (
    <div style={{ display: 'inline-block', padding: '20px' }}>
    <Frame
        animate={true}
        level={3}
        corners={4}
        layer='primary'
    >
        <div style={{ padding: '20px 40px', fontSize: '32px' }}>
            Employee Registered
        </div>
    </Frame>
</div>
);
