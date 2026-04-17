import { useState } from "react";
import API from "../../services/api";

function Upload() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Select a file");

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      await API.post("/upload", formData);

      alert("Uploaded!");
    } catch (err) {
      alert("Error uploading");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-5 rounded-2xl shadow-md">
      <h2 className="text-xl font-semibold mb-4">📄 Upload Paper</h2>

      <input
        type="file"
        className="mb-4"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
      >
        {loading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}

export default Upload;