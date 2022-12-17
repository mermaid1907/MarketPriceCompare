package com.aakin.ws.dto.converter;

import com.aakin.ws.model.Product;
import org.springframework.stereotype.Component;

@Component
public class ProductDtoConverter {

    public ProductDto convert(Product product){
        ProductDto productDto = new ProductDto();
        productDto.setProductName(product.getProductName());
        productDto.setId(product.getId());
        productDto.setPrice(product.getPrice());
        productDto.setMarketName(product.getMarketName());
        return productDto;
    }

}
