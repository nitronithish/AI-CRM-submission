import { useState } from "react";
import axios from "axios";

function InteractionForm() {
  const [doctorName, setDoctorName] = useState("");
  const [hospital, setHospital] = useState("");
  const [specialization, setSpecialization] = useState("");
  const [products, setProducts] = useState("");
  const [notes, setNotes] = useState("");

  const saveInteraction = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/save", {
        doctor_name: doctorName,
        hospital: hospital,
        specialization: specialization,
        products: products,
        notes: notes,
        ai_reply: "AI Summary will be added later"
      });

      alert("Interaction Saved Successfully!");
    } catch (error) {
      alert("Error saving interaction");
      console.log(error);
    }
  };

  return (
    <div>
      <h3>Manual Interaction Form</h3>

      <input
        type="text"
        placeholder="Doctor Name"
        value={doctorName}
        onChange={(e) => setDoctorName(e.target.value)}
      />
      <br /><br />

      <input
        type="text"
        placeholder="Hospital Name"
        value={hospital}
        onChange={(e) => setHospital(e.target.value)}
      />
      <br /><br />

      <input
        type="text"
        placeholder="Specialization"
        value={specialization}
        onChange={(e) => setSpecialization(e.target.value)}
      />
      <br /><br />

      <input type="date" />
      <br /><br />

      <input
        type="text"
        placeholder="Products Discussed"
        value={products}
        onChange={(e) => setProducts(e.target.value)}
      />
      <br /><br />

      <input type="number" placeholder="Samples Given" />
      <br /><br />

      <textarea
        placeholder="Notes"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />
      <br /><br />

      <button onClick={saveInteraction}>
        Save Interaction
      </button>
    </div>
  );
}

export default InteractionForm;