import api from "./api";

export const analyzeText = async (text) => {

  const response = await api.post("/analyze", {
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

export const analyzeVoice = async (file) => {

  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/analyze/voice",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};
export const analyzeQR = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await api.post(
        "/analyze/qr",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};