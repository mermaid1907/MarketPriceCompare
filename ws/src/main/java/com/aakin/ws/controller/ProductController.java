package com.aakin.ws.controller;
import com.aakin.ws.dto.converter.ProductDto;
import com.aakin.ws.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@RestController
@RequiredArgsConstructor
@CrossOrigin(origins = "**", allowedHeaders = "**")
public class ProductController {
    private final ProductService productService;

    @PostMapping("/upload")
    public String uploadData(@RequestParam("file") MultipartFile file) throws Exception {
        return productService.createProduct(file);
    }

    @GetMapping("/products")
    public ResponseEntity<List<ProductDto>> allProducts()
    {
       return ResponseEntity.ok(productService.findAllProducts());
    }
    @GetMapping("/products/{index}")
    public ResponseEntity<List<ProductDto>> getProductByName(@PathVariable String index) {
        return ResponseEntity.ok(productService.getProductNameContaining(index));
    }

}
