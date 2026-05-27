import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { name: '7 days ago', Contacts: 30, Responses: 10 },
  { name: '6 days ago', Contacts: 45, Responses: 12 },
  { name: '5 days ago', Contacts: 50, Responses: 15 },
  { name: '4 days ago', Contacts: 60, Responses: 18 },
  { name: '3 days ago', Contacts: 55, Responses: 16 },
  { name: '2 days ago', Contacts: 70, Responses: 22 },
  { name: 'Yesterday', Contacts: 62, Responses: 19 },
];

const PerformanceChart: React.FC = () => {
    return (
        <div style={{ width: '100%', height: 300 }}>
            <ResponsiveContainer>
                <LineChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="name" stroke="#9ca3af" />
                    <YAxis stroke="#9ca3af" />
                    <Tooltip contentStyle={{ backgroundColor: '#1f2937', border: '1px solid #374151' }} />
                    <Legend wrapperStyle={{ color: '#d1d5db' }} />
                    <Line type="monotone" dataKey="Contacts" stroke="#a78bfa" strokeWidth={2} activeDot={{ r: 8 }} />
                    <Line type="monotone" dataKey="Responses" stroke="#34d399" strokeWidth={2} />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

export default PerformanceChart;