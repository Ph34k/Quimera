import React, { useState } from 'react';

const InputField: React.FC<{label: string; type?: string; value: string | number; onChange: (e: React.ChangeEvent<HTMLInputElement>) => void; name?: string;}> = ({ label, type = "text", value, onChange, name }) => (
    <div>
        <label className="block text-sm font-medium text-dark-text-secondary">{label}</label>
        <input
            type={type}
            name={name}
            value={value}
            onChange={onChange}
            className="mt-1 block w-full bg-dark-card border border-dark-border rounded-md shadow-sm py-2 px-3 text-white focus:outline-none focus:ring-brand-light focus:border-brand-light sm:text-sm"
        />
    </div>
);

const TextAreaField: React.FC<{label: string; value: string; onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void; rows?: number}> = ({ label, value, onChange, rows=3 }) => (
    <div>
        <label className="block text-sm font-medium text-dark-text-secondary">{label}</label>
        <textarea
            value={value}
            onChange={onChange}
            rows={rows}
            className="mt-1 block w-full bg-dark-card border border-dark-border rounded-md shadow-sm py-2 px-3 text-white focus:outline-none focus:ring-brand-light focus:border-brand-light sm:text-sm"
        />
    </div>
);

const ConfigurationView: React.FC = () => {
    const [weights, setWeights] = useState({ interesting: 40, attractive: 30, single: 30 });
    const [threshold, setThreshold] = useState(7.5);
    const [hotspots, setHotspots] = useState('@bar_varginha, @academia_topfit, #varginha');
    const [persona, setPersona] = useState({ name: 'Alex', age: 29, tone: 'Casual, amigável, genuíno' });

    const handleWeightChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setWeights({ ...weights, [e.target.name]: Number(e.target.value) });
    };

    return (
        <div>
            <h1 className="text-3xl font-bold text-white mb-6">Configuration</h1>
            <div className="space-y-8 max-w-2xl">

                <div className="bg-dark-card p-6 rounded-lg shadow-lg border border-dark-border">
                    <h2 className="text-xl font-semibold text-white mb-4">Ideal Profile Criteria</h2>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-dark-text-secondary">Criteria Weights (%)</label>
                            <div className="grid grid-cols-3 gap-4 mt-1">
                                <InputField label="Interesting" type="number" name="interesting" value={weights.interesting} onChange={handleWeightChange} />
                                <InputField label="Attractive" type="number" name="attractive" value={weights.attractive} onChange={handleWeightChange} />
                                <InputField label="Single" type="number" name="single" value={weights.single} onChange={handleWeightChange} />
                            </div>
                        </div>
                        <InputField label="Qualification Threshold (0-10)" type="number" value={threshold} onChange={(e) => setThreshold(Number(e.target.value))} />
                    </div>
                </div>

                <div className="bg-dark-card p-6 rounded-lg shadow-lg border border-dark-border">
                    <h2 className="text-xl font-semibold text-white mb-4">Prospecting</h2>
                    <TextAreaField label="Digital Hotspots (comma-separated)" value={hotspots} onChange={(e) => setHotspots(e.target.value)} />
                </div>

                <div className="bg-dark-card p-6 rounded-lg shadow-lg border border-dark-border">
                    <h2 className="text-xl font-semibold text-white mb-4">System Persona</h2>
                    <div className="space-y-4">
                        <InputField label="Name" value={persona.name} onChange={(e) => setPersona({...persona, name: e.target.value})} />
                        <InputField label="Age" type="number" value={persona.age} onChange={(e) => setPersona({...persona, age: Number(e.target.value)})} />
                        <InputField label="Communication Tone" value={persona.tone} onChange={(e) => setPersona({...persona, tone: e.target.value})} />
                    </div>
                </div>

                <div className="flex justify-end">
                    <button className="bg-brand-purple text-white px-6 py-2 rounded-lg font-semibold hover:bg-brand-light transition-colors">
                        Save Configuration
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ConfigurationView;