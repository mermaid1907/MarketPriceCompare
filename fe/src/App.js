import axios from 'axios';
import './App.css';
import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container'
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'
import 'bootstrap/dist/css/bootstrap.min.css'
import React, { useEffect, useState } from 'react';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';

function App() {

  const [data, setData] = useState([]);
  const [search, setSearch] = useState('');
  console.log(search)

  useEffect(() => {
    const fethData = () => {
      fetch("http://localhost:8080/products")
      .then(response => response.json())
      .then(json => {
        setData(json)
      })
    }
    fethData();
  }, [])


  
  return (
    <div className='App'>
      <Container>
        <h1 className='text-center mt-4'>Market Price Compare</h1>
        <form>
          <InputGroup className='my-3'>
            <Form.Control onChange={(e) => setSearch(e.target.value)}
            
            placeholder='Search Product'></Form.Control>
          </InputGroup>
        </form>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Price</th>
              <th>Cheapest</th>
            </tr>
          </thead>
          <tbody>
            {data.filter((item) => {
              return search.toLowerCase() === '' ? item : item.productName.toLowerCase().includes(search);
            }).map((item) => (
              <tr>
                <td>{item.productName}</td>
                <td>{item.price}</td>
                <td>{item.marketName}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Container>
    </div>
  )
    
}

export default App;
