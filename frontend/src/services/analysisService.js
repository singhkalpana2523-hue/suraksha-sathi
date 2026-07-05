import api from "./api";

export const analyzeText = async (text) => {
  const response = await api.post("/analyze/text", {
    text,
  });

  return response.data;
};

export const analyzeImage = async (formData) => {
  const response = await api.post("/analyze/image", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const analyzeVoice = async (formData) => {
  const response = await api.post("/analyze/voice", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};