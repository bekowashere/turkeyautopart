import React, { useState, useEffect } from "react";
import products from "../products";
import { Row, Col } from "react-bootstrap";
import Product from "../components/Product";

import axios from "axios";

/* 
! useEffect yazılacak - oralar tamamlanmadı yapılmadı 

*/

function HomeScreen() {
  const [products , setProducts] = useState([])

  return (
    <div>
      <h1>Latest Products</h1>
      <Row>
        {products.map((product) => (
          <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
            <Product product={product}></Product>
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
