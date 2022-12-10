package com.aakin.ws.controller;


import com.aakin.ws.dto.ProductDto;
import com.aakin.ws.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import java.util.List;

@RestController
@RequiredArgsConstructor
public class ProductController {
    private final ProductService productService;

    @PostMapping("/upload")
    public String uploadData(@RequestParam("file") MultipartFile file) throws Exception{
        return productService.createProduct(file);
    }

    @GetMapping("/products")
    public ResponseEntity<List<ProductDto>> allProducts()
    {
       return ResponseEntity.ok(productService.findAllProducts());
    }



}
