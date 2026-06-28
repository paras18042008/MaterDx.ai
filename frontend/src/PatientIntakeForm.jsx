import { useState } from "react";

function PatientIntakeForm({ onComplete }) {
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    sex: "",
    height: "",
    weight: "",
    temperature: "",
    heartRate: "",
    systolicBP: "",
    diastolicBP: "",
    respiratoryRate: "",
    spo2: "",
    bloodGlucose: "",
    painScore: "",
  });

  const [loading, setLoading] = useState(false);
  

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  //  THIS WILL CONNECT TO BACKEND LATER (SAFE PLACEHOLDER)
const handleBeginAI = () => {
  onComplete(formData);
};


  // ---------------- UI ----------------
  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="max-w-5xl mx-auto">

        {/* Header */}
        <h1 className="text-3xl font-bold text-blue-600 mb-6">
          MaterDx.ai
        </h1>

        <h2 className="text-xl font-semibold mb-6">
          Patient Intake
        </h2>

        

        {/* Grid Layout */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* Patient Info */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold mb-4">Patient Information</h3>

            <input
              className="w-full p-2 border rounded mb-3"
              name="name"
              placeholder="Full Name"
              onChange={handleChange}
              value={formData.name}
            />

            <input
              className="w-full p-2 border rounded mb-3"
              name="age"
              type="number"
              placeholder="Age"
              onChange={handleChange}
              value={formData.age}
            />

            <select
              className="w-full p-2 border rounded mb-3"
              name="sex"
              onChange={handleChange}
              value={formData.sex}
            >
              <option value="">Sex</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>

            <input
              className="w-full p-2 border rounded mb-3"
              name="height"
              placeholder="Height (cm)"
              onChange={handleChange}
              value={formData.height}
            />

            <input
              className="w-full p-2 border rounded"
              name="weight"
              placeholder="Weight (kg)"
              onChange={handleChange}
              value={formData.weight}
            />
          </div>

          {/* Vitals */}
          <div className="bg-white p-5 rounded-xl shadow">
            <h3 className="font-semibold mb-4">Vitals</h3>

            <input
              className="w-full p-2 border rounded mb-3"
              name="temperature"
              placeholder="Temperature °C"
              onChange={handleChange}
              value={formData.temperature}
            />

            <input
              className="w-full p-2 border rounded mb-3"
              name="heartRate"
              placeholder="Heart Rate BPM"
              onChange={handleChange}
              value={formData.heartRate}
            />

            <div className="flex gap-2 mb-3">
              <input
                className="w-full p-2 border rounded"
                name="systolicBP"
                placeholder="Systolic BP"
                onChange={handleChange}
                value={formData.systolicBP}
              />

              <input
                className="w-full p-2 border rounded"
                name="diastolicBP"
                placeholder="Diastolic BP"
                onChange={handleChange}
                value={formData.diastolicBP}
              />
            </div>

            <input
              className="w-full p-2 border rounded mb-3"
              name="respiratoryRate"
              placeholder="Respiratory Rate"
              onChange={handleChange}
              value={formData.respiratoryRate}
            />

            <input
              className="w-full p-2 border rounded mb-3"
              name="spo2"
              placeholder="SpO₂ %"
              onChange={handleChange}
              value={formData.spo2}
            />

            <input
              className="w-full p-2 border rounded mb-3"
              name="bloodGlucose"
              placeholder="Blood Glucose"
              onChange={handleChange}
              value={formData.bloodGlucose}
            />

            <input
              className="w-full p-2 border rounded"
              name="painScore"
              placeholder="Pain Score (0-10)"
              onChange={handleChange}
              value={formData.painScore}
            />
          </div>
        </div>

        {/* Button */}
        <div className="mt-6 text-center">
          <button
            onClick={handleBeginAI}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
          >
            {loading ? "Preparing AI..." : "Begin AI Consultation"}
          </button>
        </div>

      </div>
    </div>
  );
}

export default PatientIntakeForm;