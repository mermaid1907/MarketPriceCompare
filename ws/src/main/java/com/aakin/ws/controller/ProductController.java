package com.aakin.ws.controller;


import com.aakin.ws.model.Product;
import com.aakin.ws.repository.ProductRepository;
import com.aakin.ws.service.ProductService;
import com.univocity.parsers.common.record.Record;
import com.univocity.parsers.csv.CsvParser;
import com.univocity.parsers.csv.CsvParserSettings;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequiredArgsConstructor
public class ProductController {
    private final ProductRepository productRepository;
    private final ProductService productService;

    @PostMapping("/upload")
    public String uploadData(@RequestParam("file") MultipartFile file) throws Exception{
        List<Product> productList = new ArrayList<>();
        InputStream inputStream = file.getInputStream();
        CsvParserSettings settings = new CsvParserSettings();
        settings.setHeaderExtractionEnabled(true);
        CsvParser parser = new CsvParser(settings);
        List<Record> parseAllRecords = parser.parseAllRecords(inputStream);
        parseAllRecords.forEach(record -> {
            Product product = new Product();
            product.setProductName(record.getString("Product Name"));
            product.setPrice(Double.parseDouble(record.getString("Price")));
            product.setMarketId(Double.parseDouble(record.getString("market_id")));
            productList.add(product);
        });
        productRepository.saveAll(productList);
        return "Upload Succesfully";
    }
    @GetMapping("/products")
    public List<Product> fetchDepartmentList()
    {
        return productService.fetchProductList();
    }

}
