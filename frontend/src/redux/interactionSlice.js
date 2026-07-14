import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",
  initialState: {
    doctorName: "",
    hospital: "",
    specialization: "",
    products: "",
    samples: "",
    notes: "",
  },
  reducers: {},
});

export default interactionSlice.reducer;