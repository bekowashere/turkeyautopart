import React from "react";
import { Card } from "react-bootstrap";
import Rating from './Rating'

import { Link } from 'react-router-dom'

/* 
! sayfa yenilenmesini önlemek için reacte uygun hale getirmeliyiz ( a etiketleri yerine Link )
TODO: react-router-dom import Link

*/


function Product({ product }) {
  return (
    <Card className="my-3 p-3 rounded">
      <Link to={`/product/${product._id}`}>
        <Card.Img src={product.image} />

        <Card.Body>
          <Link to={`/product/${product._id}`}>
            <Card.Title as="div">
              <strong>{product.name}</strong>
            </Card.Title>
          </Link>

          <Card.Text as="div">
            <div className="my-3">
              {product.rating} from {product.numReviews}
              <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'}></Rating>
            </div>
          </Card.Text>

          <Card.Text as="h3">${product.price}</Card.Text>
        </Card.Body>
      </Link>
    </Card>
  );
}

export default Product;
