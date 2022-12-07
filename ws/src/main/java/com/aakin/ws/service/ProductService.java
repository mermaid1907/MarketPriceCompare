package com.aakin.ws.service;

import com.aakin.ws.model.Product;
import com.aakin.ws.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ProductService {
    private final ProductRepository productRepository;

    public List<Product> fetchProductList()
    {
        return (List<Product>) productRepository.findAll();
    }
}
