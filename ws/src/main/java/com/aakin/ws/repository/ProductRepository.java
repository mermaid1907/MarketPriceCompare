package com.aakin.ws.repository;

import com.aakin.ws.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;


@Repository
public interface ProductRepository extends JpaRepository<Product, String> {
    List<Product> findByProductNameContaining(String title); //%like//
    List<Product> findByProductNameContains(String title); //%like%
    List<Product> findByProductNameIsContaining(String title); //like%
}
