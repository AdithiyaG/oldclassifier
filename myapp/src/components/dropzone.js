import React,{useState}from 'react';
import Dropzone from 'react-dropzone'



export default function Drop() {
    const [fileNames, setFileNames] = useState([]);
    const handleDrop = acceptedFiles =>
      setFileNames(acceptedFiles.map(file => file.name));
  
    return (
      <div className="App">
        <Dropzone onDrop={handleDrop}>
          {({ getRootProps, getInputProps }) => (
            <div {...getRootProps({ className: "dropzone" })}>
              <input {...getInputProps()} />
              <p>Drag'n'drop files, or click to select files</p>
            </div>
          )}
        </Dropzone>
        <div>
          <strong>Files:</strong>
          <ul>
            {fileNames.map(fileName => (
              <li key={fileName}>{fileName}</li>
            ))}
          </ul>
        </div>
      </div>
    );
            }